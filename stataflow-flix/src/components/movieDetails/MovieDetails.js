import React, { useState, useEffect } from "react"import {
  Grid,
  Box,
  Typography,
  Container,
  Hidden,
  withWidth,
  makeStyles,
  TextField,
  CircularProgress,
  Paper,
  Button,
} from "@material-ui/core";
import MovieCoverPoster from "components/movieDetails/images/MovieCoverPoster.jpg";
import ActorList from "components/movieDetails/ActorList";
import DirectorList from "components/movieDetails/DirectorList";
import ReviewList from "components/movieDetails/ReviewList";
import PropTypes from "prop-types";
import StarsIcon from "@material-ui/icons/Stars";
import axios from "axios";
import RatingStars from "components/home/MovieCard/RatingStars";

const useStyles = makeStyles(() => ({
  circularProgress: {
    color: "#FDA74A",
  },
  moviePoster: {
    height: "345px",
    width: "230px",
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
    width: "80%",
    marginBottom: "2em",
    marginRight: "0.5em",
  },
}));

function MovieDetails(props) {
  const { location, userID, apiURL } = props;
  const movieData = location.state.movieData;
  const classes = useStyles();
  const [isLoading, setLoading] = useState(true);
  const [reviews, setReviews] = useState([]);
  const [reviewText, setReviewText] = useState("");
  const [rating, setRating] = useState(null);
  const moviePoster = MovieCoverPoster;

  useEffect(() => {
    setTimeout(() => {
      setLoading(false);
    }, 500);
  });

  async function postReview() {
    let reviewData = {
      userID: userID,
      movie: movieData.title,
      rating: rating !== 0 ? rating : null,
      reviewText: reviewText,
    };
    let config = {
      method: "post",
      url: `${apiURL}/reviews`,
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      data: reviewData,
    };
    if (reviewText !== "") setReviews([...reviews, reviewData]);
    setReviewText("");
    let res = await axios(config);
    console.log(res);
  }

  function postRating(rating) {
    setRating(rating);
    setTimeout(() => {
      postReview();
    }, 5000);
  }

  function handleRemoveReview(id) {
    setReviews(reviews.filter((review) => review.reviewID !== id));
  }

  return isLoading ? (
    <Container
      fixed
      maxWidth={"lg"}
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        height: "calc(100vh - 64px)",
      }}
    >
      <CircularProgress className={classes.circularProgress} />
    </Container>
  ) : (
    <Container fixed maxWidth={"lg"}>
      <Grid container style={{ marginTop: "5em" }}>
        <Hidden smDown>
          <Grid
            item
            xs={12}
            sm={12}
            md={4}
            lg={3}
            style={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            {moviePoster ? (
              <Paper
                elevation={2}
                style={{
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: "5px",
                }}
              >
                <img
                  src={moviePoster}
                  alt={movieData.title}
                  className={classes.moviePoster}
                />
              </Paper>
            ) : (
              <Box
                className={classes.moviePoster}
                style={{
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                  flexWrap: true,
                  background: "#707070AA",
                  borderRadius: "5px",
                  color: "#F8F8F8",
                }}
              >
                <Typography variant="h1">?</Typography>
              </Box>
            )}
          </Grid>
        </Hidden>
        <Grid item xs={12} sm={12} md={8} lg={9}>
          <Typography gutterBottom variant="h3">
            {movieData.title}
          </Typography>
          <Typography gutterBottom variant="h5">
            {movieData.genres.map((genre, index) => {
              return index === movieData.genres.length - 1
                ? genre
                : `${genre} / `;
            })}
          </Typography>
          <Box style={{ display: "flex" }}>
            <Typography
              gutterBottom
              variant="h6"
              style={{ marginRight: "1.5em" }}
            >
              {movieData.releaseYear}
            </Typography>
            <Typography variant="h6" style={{ marginRight: "1.5em" }}>
              {`${Math.floor(movieData.runtimeMinutes / 60)}hr  ${
                movieData.runtimeMinutes % 60
              }mins`}
            </Typography>
            <StarsIcon style={{ marginTop: "3px", marginRight: "5px" }} />
            <Typography
              gutterBottom
              variant="h6"
              style={{ marginRight: "1.5em" }}
            >
              {movieData.averageRating}
            </Typography>
          </Box>
          <Typography gutterBottom variant="subtitle1">
            Revenue: ${movieData.revenue} million
          </Typography>
          <Typography gutterBottom variant="h6" style={{ marginTop: "1em" }}>
            Description:
          </Typography>
          <Typography variant="body1">{movieData.description}</Typography>
        </Grid>
      </Grid>
      <Grid container style={{ margin: "5em 0em" }}>
        <Grid item xs={12} sm={12} md={8} lg={9}>
          <Typography gutterBottom variant="h4">
            Reviews
          </Typography>
          <RatingStars postRating={postRating} />
          <Box style={{ display: "flex", marginTop: "0.5em" }}>
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
                  postReview();
                }
              }}
              className={classes.reviewTextInput}
              fullWidth={false}
            />
            <Button
              color="primary"
              style={{ height: "50%", marginTop: "1em" }}
              onClick={() => postReview()}
            >
              POST
            </Button>
          </Box>
          <ReviewList
            reviewsList={reviews}
            handleRemoveReview={handleRemoveReview}
            userID={userID}
          />
        </Grid>
        <Grid item xs={12} sm={12} md={4} lg={3}>
          <Typography variant="h4">Directors</Typography>
          <DirectorList directorsList={movieData.directors} />
          <Typography variant="h4" style={{ marginTop: "1em" }}>
            Actors
          </Typography>
          <ActorList actorsList={movieData.actors} />
        </Grid>
      </Grid>
    </Container>
  );
}

MovieDetails.propTypes = {
  width: PropTypes.oneOf(["lg", "md", "sm", "xl", "xs"]).isRequired,
};

export default withWidth()(MovieDetails);
