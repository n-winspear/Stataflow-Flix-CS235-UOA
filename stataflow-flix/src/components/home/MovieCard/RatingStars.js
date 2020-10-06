import React, { useState, useEffect } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Rating from "@material-ui/lab/Rating";
import Box from "@material-ui/core/Box";

const labels = {
  0.5: "Boring",
  1: "Boring",
  1.5: "Bland",
  2: "Bland",
  2.5: "Weak",
  3: "Weak",
  3.5: "Poor",
  4: "Poor",
  4.5: "Average",
  5: "Average",
  5.5: "Fair",
  6: "Fair",
  6.5: "Good",
  7: "Great",
  7.5: "Good",
  8: "Good",
  8.5: "Superb",
  9: "Superb",
  9.5: "Fantastic",
  10: "Fantastic",
};

const useStyles = makeStyles({
  root: {
    width: 200,
    display: "flex",
    alignItems: "center",
  },
});

export default function RatingStars(props) {
  const [value, setValue] = useState(0);
  const [hover, setHover] = useState(-1);
  const { postRating, userRating, movieTitle } = props;
  const classes = useStyles();

  useEffect(() => {
    if (value === 0 && userRating) {
      setValue(userRating.rating);
    } else if (value !== 0 && userRating) {
      postRating({
        ratingID: userRating.ratingID,
        rating: value,
        movieTitle: movieTitle,
      });
    } else if (value !== 0 && !userRating) {
      postRating({
        ratingID: null,
        rating: value,
        movieTitle: movieTitle,
      });
    }
  });

  return (
    <div className={classes.root}>
      <Rating
        name="movie-rating"
        max={10}
        value={value}
        precision={0.5}
        onChange={async (event, newValue) => {
          await setValue(newValue);
        }}
        onChangeActive={(event, newHover) => {
          setHover(newHover);
        }}
      />
      {value !== null && (
        <Box ml={2}>{labels[hover !== -1 ? hover : value]}</Box>
      )}
    </div>
  );
}
