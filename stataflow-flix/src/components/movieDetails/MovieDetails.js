import React, { useState, useEffect } from "react";
import { Grid, Box, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import CircularProgress from "@material-ui/core/CircularProgress";
import MovieCoverPoster from "components/movieDetails/images/MovieCoverPoster.jpg";
import StarRateIcon from "@material-ui/icons/StarRate";
import ActorList from "components/movieDetails/ActorList";
import ReviewList from "./ReviewList";
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
      <Grid container justify="center" alignItems="flex-start">
        <Grid
          container
          direction="column"
          justify="center"
          alignItems="center"
          item
          xs={12}
          sm={6}
          md={4}
          lg={3}
          xl={2}
        >
          <Grid item xs={false} sm={12}>
            <Box className={classes.movieCoverPoster}>
              <img
                src={MovieCoverPoster}
                alt={"Movie Cover"}
                height={"100%"}
                width={"auto"}
              />
            </Box>
            <Box mt={2} ml={1}>
              <Typography variant="subtitle1">Genres:</Typography>
              <Typography gutterBottom variant="h5">
                {movieData.genres.map((genre, index) => {
                  let genreText =
                    index === movieData.genres.length - 1
                      ? genre
                      : `${genre},  `;
                  return genreText;
                })}
              </Typography>
            </Box>
          </Grid>
        </Grid>
        <Grid
          container
          direction="column"
          justify="flex-start"
          alignItems="flex-start"
          className={classes.movieInformation}
          item
          xs={12}
          sm={6}
          md={8}
          lg={9}
          xl={9}
        >
          <Grid item xs={12} className={classes.movieTitle}>
            <Typography gutterBottom variant="h2">
              {movieData.title}
            </Typography>
          </Grid>
          <Grid item xs={1}>
            <Box className={classes.movieDetails}>
              <Typography variant="h5">{movieData.releaseYear}</Typography>
              <Typography variant="h5">{`${Math.floor(
                movieData.runtimeMinutes / 60
              )}hr ${movieData.runtimeMinutes % 60}min`}</Typography>
              <Box className={classes.averageRating}>
                <StarRateIcon />
                <Typography variant="h5">{movieData.averageRating}</Typography>
              </Box>
            </Box>
          </Grid>
          <Grid item xs={12}>
            <Typography variant="h6">Description:</Typography>
            <Typography gutterBottom>{movieData.description}</Typography>
          </Grid>
          <Grid
            container
            direction="row"
            justify="flex-start"
            alignItems="flex-start"
            className={classes.actorsReviews}
          >
            <Grid
              container
              direction="column"
              item
              xs={12}
              sm={6}
              md={4}
              lg={3}
              xl={2}
            >
              <Typography gutterBottom variant="h5">
                Actors
              </Typography>
              <ActorList actorsList={movieData.actors} />
            </Grid>
            <Divider orientation="vertical" flexItem />
            <Grid
              container
              direction="column"
              item
              style={{ marginLeft: "5em" }}
              xs={12}
              sm={6}
              md={8}
              lg={9}
              xl={9}
            >
              <Typography gutterBottom variant="h5">
                Reviews
              </Typography>
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
            </Grid>
          </Grid>
        </Grid>
      </Grid>
    </Box>
  );
}
