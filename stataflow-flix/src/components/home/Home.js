import React, { useState, useEffect } from "react";
import { Grid, Box } from "@material-ui/core";
import MovieCard from "components/home/MovieCard/MovieCard";
import { makeStyles } from "@material-ui/core/styles";
import axios from "axios";
import CircularProgress from "@material-ui/core/CircularProgress";
import { Tab } from "@material-ui/icons";

const useStyles = makeStyles(() => ({
  loading: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    flexGrow: 1,
    height: "calc(100vh - 64px)",
  },
  grid: {
    width: "100%",
    margin: 0,
  },
  circularProgress: {
    color: "#FDA74A",
  },
}));

export default function Home(props) {
  const classes = useStyles();
  const { apiURL, userID } = props;
  const [isLoading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);
  const [ratings, setRatings] = useState({
    ratingsUpdated: false,
    ratingList: [],
    ratedMovies: [],
  });

  useEffect(() => {
    if (movies.length === 0) {
      async function getMovies() {
        let config = {
          method: "get",
          url: `${apiURL}/movies`,
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
            "Access-Control-Allow-Origin": "*",
          },
        };
        let res = await axios(config);
        let tempShortMoviesList = res.data.movies.slice(0, 50);
        //setMovies(res.data.movies);
        setMovies(tempShortMoviesList);
      }
      getMovies();
    }
    if (!ratingsUpdated) {
      async function getRatings() {
        let config = {
          method: "get",
          url: `${apiURL}/ratings`,
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
            "Access-Control-Allow-Origin": "*",
          },
        };
        let res = await axios(config);
        let ratings = res.data.ratings;
        let ratedMovies = await ratings.map((rating) => {
          result = [];
          if (rating.userID === userID) {
            result.push(rating);
          }
          return result;
        });
        setRatings({
          ratingsUpdated: true,
          ratingList: ratings,
          ratedMovies: ratedMovies,
        });
      }
      getRatings();
    }
    if (movies.length > 0 && ratings.length > 0) {
      setLoading(!isLoading);
    }
  });

  async function postRating(ratingPostData) {
    const { ratingID, rating, movieTitle } = ratingPostData;
    if (ratingID) {
      let config = {
        method: "put",
        url: `${apiURL}/ratings/${ratingID}`,
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        data: {
          userID: userID,
          movieTitle: movieTitle,
          rating: rating,
        },
      };
      let res = await axios(config);
      console.log(res);
    } else {
      let config = {
        method: "post",
        url: `${apiURL}/ratings`,
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        data: {
          userID: userID,
          movieTitle: movieTitle,
          rating: rating,
        },
      };
      let res = await axios(config);
      console.log(res);
    }
    setRatings({
      ...ratings,
      ratingsUpdated: false,
    });
  }

  function viewMovie(movieData, rating) {
    const URL = movieData.movieTitle.toLowerCase().replace(/\s/g, "-");
    props.history.push({
      pathname: `/movies/${URL}`,
      state: {
        apiURL: apiURL,
        userID: userID,
        movieData: movieData,
        userRating: rating,
        postRating: postRating,
      },
    });
  }

  return isLoading ? (
    <Box className={classes.loading}>
      <CircularProgress className={classes.circularProgress} />
    </Box>
  ) : (
    <Grid className={classes.grid} container spacing={3}>
      {movies.map((movieData) => {
        let userRating = ratings.ratingList.map((rating) => {
          return rating.userID === userID ? rating : null;
        });

        return (
          <Grid
            container
            item
            justify="center"
            key={movieData.movieID}
            xs={12}
            sm={6}
            md={4}
            lg={3}
            xl={2}
          >
            <MovieCard
              movieData={movieData}
              apiURL={apiURL}
              viewMovie={viewMovie}
              postRating={postRating}
              userRating={userRating}
            />
          </Grid>
        );
      })}
    </Grid>
  );
}
