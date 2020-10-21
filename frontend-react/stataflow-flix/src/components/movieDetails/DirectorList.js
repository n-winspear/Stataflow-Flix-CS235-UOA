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
  listItemDirector: {
    paddingLeft: '2px', 
    '&:hover': {
      cursor: 'pointer',
      backgroundColor: '#0000000F'
    }
  }
}));

export default function DirectorList(props) {
  const { directorsList, movieImagesApi, movieBaseApi, apiKey } = props;
  const classes = useStyles();
  const [imagesLoaded, setImagesLoaded] = useState(false)
  const [directorsProfiles, setDirectorsProfiles] = useState([])

  useEffect(() => {
    if (!imagesLoaded) {
      async function getDirectorImages() {
        let tempList = await Promise.all(directorsList.map(async (director) => {
          let config = {
            method: "get",
            url: `${movieBaseApi}/search/person?api_key=${apiKey}&query=${director.fullName}&page=1`,
          };
          let res = await axios(config);
          let detConf = {
            method: "get",
            url: `${movieBaseApi}/person/${res.data.results[0].id}?api_key=${apiKey}`,
          }
          let dets = await axios(detConf)
          return({fullName: director.fullName, profilePath: `${movieImagesApi}${res.data.results[0].profile_path}`, birthday: dets.data.birthday, imdbId: dets.data.imdb_id ? `name/${dets.data.imdb_id}` : ""})
        }))
        setDirectorsProfiles(tempList)
        setImagesLoaded(true)
      }
      getDirectorImages()
    }
  })

  return (
    <List className={classes.root}>
      {directorsProfiles.map((director, index) => {
        console.log(directorsProfiles)
        return (
          <ListItem key={index} className={classes.listItemDirector} onClick={() => window.location.href=`https://www.imdb.com/${director.imdbId}`}>
            <ListItemAvatar>
              <Avatar src={director.profilePath} alt={director.fullName} />
            </ListItemAvatar>
            <ListItemText 
              primary={director.fullName}
              secondary={director.birthday ? `${new Date().getFullYear() - parseInt(director.birthday.slice(0, 4), 10)} years old`: ""}
            />
          </ListItem>
        );
      })}
    </List>
  )
}
