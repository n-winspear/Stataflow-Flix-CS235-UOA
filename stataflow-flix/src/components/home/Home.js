import React, { useState, useEffect } from "react";
import { Grid, Box } from "@material-ui/core";
import MovieCard from "components/home/MovieCard/MovieCard";
import { makeStyles } from "@material-ui/core/styles";
import axios from "axios";
import CircularProgress from "@material-ui/core/CircularProgress";

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

  useEffect(() => {
    if (movies.length === 0) {
      async function getMovies() {
        let config = {
          method: "get",
          url: `${apiURL}/movies`,
        };
        let res = await axios(config);
        let tempShortMoviesList = res.data.movies.slice(0, 50);
        //setMovies(res.data.movies);
        setMovies(tempShortMoviesList);
        setLoading(false);
      }
      getMovies();
    }
  }, [movies.length, apiURL, userID, isLoading]);

  function viewMovie(movieData) {
    const URL = movieData.movieTitle.toLowerCase().replace(/\s/g, "-");
    props.history.push({
      pathname: `/movies/${URL}`,
      state: {
        apiURL: apiURL,
        userID: userID,
        movieData: movieData,
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
              userID={userID}
              viewMovie={viewMovie}
            />
          </Grid>
        );
      })}
    </Grid>
  );
}
