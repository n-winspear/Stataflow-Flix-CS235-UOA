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
          url: `${apiURL}/movies/all`,
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
        setLoading(false);
      }
      getMovies();
    }
  });

  function viewMovie(movieData) {
    const URL = movieData.title.toLowerCase().replace(/\s/g, "-");

    //THIS IS WHERE THE CODE GOES TO GET THE MOVIES DATA BASED ON ID

    props.history.push({
      pathname: `/movie/${URL}`,
      state: {
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
            key={movieData.id}
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
            />
          </Grid>
        );
      })}
    </Grid>
  );
}
