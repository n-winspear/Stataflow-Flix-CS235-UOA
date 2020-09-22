import React, { useState, useEffect } from "react";
import { Box, Grid } from "@material-ui/core";
import MovieCard from "components/home/MovieCard";
import { makeStyles } from "@material-ui/core/styles";
import axios from "axios";
import CircularProgress from "@material-ui/core/CircularProgress";

let apiVersion = 1;
let api_URL = `http://127.0.0.1:5000/api/v${apiVersion}`;

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    alignItems: "center",
    justifyContent: "flex-end",
    flexGrow: 1,
    padding: theme.spacing(3),
    backgroundColor: "#F1F1F1",
  },
}));

export default function Home(props) {
  const classes = useStyles();
  const [isLoading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    async function getHomeData() {
      let config = {
        method: "get",
        url: `${api_URL}/home`,
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          "Access-Control-Allow-Origin": "http//localhost:3000",
        },
      };

      let res = await axios(config);
      let tempShortMoviesList = res.data.movies.slice(0, 100);
      //setMovies(res.data.movies);
      setMovies(tempShortMoviesList);
      setLoading(false);
    }
    getHomeData();
  });

  return isLoading ? (
    <CircularProgress />
  ) : (
    <Box className={classes.root}>
      <Grid container justify={"center"} spacing={2}>
        {movies.map((movieData, index) => {
          return (
            <Grid key={index} item xs={12} sm={6} md={4} lg={3} xl={2}>
              <MovieCard movieData={movieData} />
            </Grid>
          );
        })}
      </Grid>
    </Box>
  );
}
