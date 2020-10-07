import React, { useState, useEffect } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Rating from "@material-ui/lab/Rating";
import Box from "@material-ui/core/Box";
import axios from "axios";

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
  const [rating, setRating] = useState(null);
  const { movieTitle, apiURL, userID } = props;
  const classes = useStyles();

  useEffect(() => {
    async function getRating() {
      let config = {
        method: "get",
        url: `${apiURL}/ratings`,
      };
      let res = await axios(config);
      let ratings = res.data.ratings;
      await ratings.forEach((rating) => {
        if (rating.userID === userID && rating.movieTitle === movieTitle) {
          setRating(rating);
        }
      });
    }
    getRating();
  }, [value, movieTitle, apiURL, userID]);

  async function postRating(ratingValue) {
    if (rating) {
      let config = {
        method: "put",
        url: `${apiURL}/ratings/${rating.ratingID}`,
        headers: {
          "Content-Type": "application/json",
        },
        data: {
          userID: rating.userID,
          movieTitle: movieTitle,
          rating: ratingValue,
        },
      };
      let res = await axios(config);
      console.log(res);
      setValue(ratingValue);
    } else {
      let config = {
        method: "post",
        url: `${apiURL}/ratings`,
        headers: {
          "Content-Type": "application/json",
        },
        data: {
          userID: userID,
          movieTitle: movieTitle,
          rating: rating,
        },
      };
      let res = await axios(config);
      console.log(res);
      setValue(ratingValue);
    }
  }

  return (
    <div className={classes.root}>
      <Rating
        name="movie-rating"
        max={10}
        value={value}
        precision={0.5}
        onChange={async (event, newValue) => {
          await postRating(newValue);
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
