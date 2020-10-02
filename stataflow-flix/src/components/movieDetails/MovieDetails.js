import React, { useState, useEffect } from "react";
import { Grid, Box, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import CircularProgress from "@material-ui/core/CircularProgress";
import MovieCoverPoster from "components/movieDetails/images/MovieCoverPoster.jpg";
import StarRateIcon from "@material-ui/icons/StarRate";
import ActorList from "components/movieDetails/ActorList";
import ReviewList from "components/movieDetails/ReviewList";
import { TextField } from "@material-ui/core";
import { v4 as uuidv4 } from "uuid";
import Divider from "@material-ui/core/Divider";

const useStyles = makeStyles(() => ({
  pageContent: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    flexGrow: 1,
    height: "calc(100vh - 64px)",
  },
  circularProgress: {
    color: "#FDA74A",
  },
  movieCoverPoster: {
    height: "505px",
    width: "350px",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  },
  movieTitle: {
    width: "45em",
    marginTop: "2em",
  },
  movieDetails: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    width: "18em",
    marginBottom: "5em",
  },
  movieInformation: {
    width: "100%",
  },
  averageRating: {
    display: "flex",
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    width: "2em",
  },
  actorsReviews: {
    marginTop: "5em",
  },
  reviewTextInput: {
    width: "50%",
  },
}));

export default function MovieDetails(props) {
  const { location } = props;
  const movieData = location.state.movieData;
  const classes = useStyles();
  const [isLoading, setLoading] = useState(true);
  const [reviews, setReviews] = useState([]);
  const [reviewText, setReviewText] = useState("");

  useEffect(() => {
    function loadData() {
      setTimeout(() => {
        setLoading(false);
      }, 1000);
    }
    loadData();
  });

  function handleRemoveReview(id) {
    setReviews(reviews.filter((review) => review.id !== id));
  }

  return isLoading ? (
    <Box className={classes.pageContent}>
      <CircularProgress className={classes.circularProgress} />
    </Box>
  ) : (
    <Box className={classes.pageContent}>
      <ActorList actorsList={movieData.actors} />
      <TextField
        id="add-review"
        label="Add Review"
        placeholder="Write your review here..."
        multiline
        value={reviewText}
        onChange={(e) => setReviewText(e.target.value)}
        onKeyPress={(e) => {
          if (e.key === "Enter") {
            e.preventDefault();
            setReviews([
              ...reviews,
              {
                id: uuidv4(),
                reviewText: reviewText,
              },
            ]);
            setReviewText("");
          }
        }}
        className={classes.reviewTextInput}
        fullWidth={false}
      />
      <ReviewList
        reviewsList={reviews}
        handleRemoveReview={handleRemoveReview}
      />
    </Box>
  );
}
