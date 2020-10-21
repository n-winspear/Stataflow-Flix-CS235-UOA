import React, { useEffect, useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import ListItemAvatar from "@material-ui/core/ListItemAvatar";
import Avatar from "@material-ui/core/Avatar";
import axios from 'axios'

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
    maxWidth: 360,
    backgroundColor: theme.palette.background.paper,
  },
  listItemActor: {
    paddingLeft: '2px', 
    '&:hover': {
      cursor: 'pointer',
      backgroundColor: '#0000000F'
    }
  }
}));

export default function ActorList(props) {
  const { actorsList, movieImagesApi, movieBaseApi, apiKey } = props;
  const classes = useStyles();
  const [imagesLoaded, setImagesLoaded] = useState(false)
  const [actorsProfiles, setActorsProfiles] = useState([])

  useEffect(() => {
    if (!imagesLoaded) {
      async function getActorImages() {
        let tempList = await Promise.all(actorsList.map(async (actor) => {
          let config = {
            method: "get",
            url: `${movieBaseApi}/search/person?api_key=${apiKey}&query=${actor.fullName}&page=1`,
          };
          let res = await axios(config);
          let detConf = {
            method: "get",
            url: `${movieBaseApi}/person/${res.data.results[0].id}?api_key=${apiKey}`,
          }
          let dets = await axios(detConf)
          return({fullName: actor.fullName, profilePath: `${movieImagesApi}${res.data.results[0].profile_path}`, birthday: dets.data.birthday, imdbId: dets.data.imdb_id ? `name/${dets.data.imdb_id}` : ""})
        }))
        setActorsProfiles(tempList)
        setImagesLoaded(true)
      }
      getActorImages()
    }
  })

  return (
    <List className={classes.root}>
      {actorsProfiles.map((actor, index) => {
        console.log(actorsProfiles)
        return (
          <ListItem key={index} className={classes.listItemActor} onClick={() => window.location.href=`https://www.imdb.com/${actor.imdbId}`}>
            <ListItemAvatar>
              <Avatar src={actor.profilePath} alt={actor.fullName} />
            </ListItemAvatar>
            <ListItemText 
              primary={actor.fullName}
              secondary={actor.birthday ? `${new Date().getFullYear() - parseInt(actor.birthday.slice(0, 4), 10)} years old`: ""}
            />
          </ListItem>
        );
      })}
    </List>
  )
}


/*

JUST TRY AND MAKE AN IMAGE DISPLAY OR TRY A DIV WITH A BACKGROUND IMAGE STYLE

Add iN A BACK BUTTON WHEN LOOKING AT MOVIE DETAILS

*/
