import React, { useState, useEffect } from "react";
import { Grid, Box, Button } from "@material-ui/core";
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
  showMore: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    margin: '1em 0em'
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
  const [remainingMovies, setRemainingMovies] = useState([])
  const [slice, setSlice] = useState(0)
  const [loadingMovies, setLoadingMovies] = useState(false)

  useEffect(() => {
    if (movies.length === 0) {
      async function getMovies() {
        let config = {
          method: "get",
          url: `${apiURL}/movies`,
        };
        let res = await axios(config);
        switch(true) {
          case window.screen.width < 600:
            setSlice(50)
            break;
          case window.screen.width < 960:
            setSlice(50)
            break;
          case window.screen.width < 1280:
            setSlice(51)
            break;
          case window.screen.width < 1920:
            setSlice(52)
            break;
          default:
            setSlice(54)
            break;
        }
        setMovies(res.data.movies.slice(0, slice));
        setRemainingMovies(res.data.movies.slice(50))
        setLoading(false);
      }
      getMovies();
    }
  }, [movies, movies.length, apiURL, userID, isLoading, slice]);

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

  function loadMoreMovies() {
    setMovies([...movies, ...remainingMovies.slice(0, slice)])
    setRemainingMovies(remainingMovies.slice(slice))
    if (slice * 2 > 1000) {
      setSlice(1001)
    } else {
      setSlice(slice * 2)
    }
    setLoadingMovies(false)
  }

  return isLoading ? (
    <Box className={classes.loading}>
      <CircularProgress className={classes.circularProgress} />
    </Box>
  ) : (
    <>
      <Grid className={classes.grid} container spacing={3}>
        {movies.map((movieData, index) => {
          return (
            <Grid
              container
              item
              justify="center"
              key={index}
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
      <Box className={classes.showMore} >
        {loadingMovies ? (<CircularProgress className={classes.circularProgress} />) : (
          <Button variant="contained" style={{backgroundColor: '#FDA74A', color: '#F8F8F8'}} onClick={() => {
            setLoadingMovies(true);
            loadMoreMovies();
          }}>Load More</Button>
        )}
      </Box>
    </>
  );
}
