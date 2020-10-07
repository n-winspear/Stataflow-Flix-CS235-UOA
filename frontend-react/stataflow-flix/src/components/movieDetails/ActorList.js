import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import ListItemAvatar from "@material-ui/core/ListItemAvatar";
import Avatar from "@material-ui/core/Avatar";
import PersonIcon from "@material-ui/icons/Person";

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
    maxWidth: 360,
    backgroundColor: theme.palette.background.paper,
  },
}));

export default function ActorList(props) {
  const { actorsList } = props;
  const classes = useStyles();

  return (
    <List className={classes.root}>
      {actorsList.map((actor) => {
        return (
          <ListItem key={actor.personID} style={{ paddingLeft: "2px" }}>
            <ListItemAvatar>
              <Avatar>
                <PersonIcon />
              </Avatar>
            </ListItemAvatar>
            <ListItemText
              primary={actor.fullName}
              secondary={actor.role ? actor.role : "Character Unknown"}
            />
          </ListItem>
        );
      })}
    </List>
  );
}
