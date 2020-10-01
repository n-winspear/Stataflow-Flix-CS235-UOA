import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemAvatar from "@material-ui/core/ListItemAvatar";
import ListItemSecondaryAction from "@material-ui/core/ListItemSecondaryAction";
import ListItemText from "@material-ui/core/ListItemText";
import Avatar from "@material-ui/core/Avatar";
import IconButton from "@material-ui/core/IconButton";
import DeleteIcon from "@material-ui/icons/Delete";
import PersonIcon from "@material-ui/icons/Person";
import { Typography } from "@material-ui/core";

const useStyles = makeStyles(() => ({
  root: {
    flexGrow: 1,
    overflowY: "auto",
    maxHeight: "20em",
  },
}));

export default function ReviewList(props) {
  const { reviewsList, handleRemoveReview } = props;
  const classes = useStyles();

  return reviewsList.length > 0 ? (
    <div className={classes.root}>
      <List>
        {reviewsList.map((review) => {
          return (
            <ListItem key={review.id} style={{ alignItems: "flex-start" }}>
              <ListItemAvatar style={{ marginTop: "0.5em" }}>
                <Avatar>
                  <PersonIcon />
                </Avatar>
              </ListItemAvatar>
              <ListItemText
                primary={review.reviewText}
                primaryTypographyProps={{
                  style: {
                    whiteSpace: "normal",
                    wordWrap: "break-word",
                  },
                }}
              />
              <ListItemSecondaryAction>
                <IconButton
                  edge="end"
                  aria-label="delete"
                  onClick={() => {
                    handleRemoveReview(review.id);
                  }}
                >
                  <DeleteIcon />
                </IconButton>
              </ListItemSecondaryAction>
            </ListItem>
          );
        })}
      </List>
    </div>
  ) : (
    <></>
  );
}
