import React, { useState, useEffect } from "react";
import { Grid, Box, Button, Container } from "@material-ui/core";
import MovieCard from "components/home/MovieCard/MovieCard";
import InputBase from "@material-ui/core/InputBase";
import { fade, makeStyles } from "@material-ui/core/styles";
import SearchIcon from "@material-ui/icons/Search";
import axios from "axios";
import CircularProgress from "@material-ui/core/CircularProgress";
import Fuse from 'fuse.js'

const useStyles = makeStyles((theme) => ({
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
  search: {
    position: "relative",
    borderRadius: theme.shape.borderRadius,
    backgroundColor: fade('#707070', 0.25),
    "&:hover": {
      backgroundColor: fade('#707070', 0.35),
    },
    margin: "2em auto",
    width: "30%",
    [theme.breakpoints.up("sm")]: {
      width: "30%",
    },
  },
  searchIcon: {
    padding: theme.spacing(0, 2),
    height: "100%",
    position: "absolute",
    pointerEvents: "none",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  inputRoot: {
    color: "inherit",
  },
  inputInput: {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)}px)`,
    transition: theme.transitions.create("width"),
    width: "100%",
    [theme.breakpoints.up("sm")]: {
      width: "30ch",
      "&:focus": {
        width: "60ch",
      },
    },
  },
}));

export default function Home(props) {
  const classes = useStyles();
  const { apiURL, userID,  } = props;
  const [isLoading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);
  const [allMovies, setAllMovies] = useState([])
  const [slice, setSlice] = useState(0)
  const [canLoadMovies, setCanLoadMovies] = useState(false)
  let typingTimer;

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
        setAllMovies(res.data.movies);
        setMovies(res.data.movies.slice(0, slice));
        setLoading(false);
      }
      getMovies();
    }
  }, [movies, movies.length, apiURL, userID, isLoading, slice]);

  function searchMovie(text) {

    const options = {
      includeScore: true,
      shouldSort: true,
      findAllMatches: true,
      threshold: 0.4,
      minMatchCharLength: 3,
      keys: ['movieTitle']      
    }

    const fuse = new Fuse(allMovies, options)

    const result = fuse.search(text)
    setMovies(result.map(movie => movie.item))
  }

  function viewMovie(movieData, movieImagesApi) {
    const URL = movieData.movieTitle.toLowerCase().replace(/\s/g, "-");
    props.history.push({
      pathname: `/movies/${URL}`,
      state: {
        apiURL: apiURL,
        userID: userID,
        movieData: movieData,
        movieImagesApi: movieImagesApi
      },
    });
  }

  function loadMoreMovies() {
    let newSlice = slice;
    if (newSlice * 2 > 1000) {
      newSlice = 1001
      setCanLoadMovies(false)
    } else {
      newSlice = newSlice * 2
    }
    setMovies(allMovies.slice(0, newSlice))
    setSlice(newSlice)
  }

  return isLoading ? (
    <Box className={classes.loading}>
      <CircularProgress className={classes.circularProgress} />
    </Box>
  ) : (
    <>
      <Container >
        <div className={classes.search}>
          <div className={classes.searchIcon}>
            <SearchIcon />
          </div>
          <InputBase
            placeholder="Search…"
            classes={{
              root: classes.inputRoot,
              input: classes.inputInput,
            }}
            inputProps={{ "aria-label": "search" }}
            onKeyUp={(e)=> {
              clearTimeout(typingTimer)
              if (e.target.value) {
                e.persist()
                typingTimer = setTimeout(() => {
                  searchMovie(e.target.value)
                }, 1000)
              }
            }}
          />
        </div>
      </Container>
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
        {canLoadMovies ? (<></>) : (
          <Button variant="contained" style={{backgroundColor: '#FDA74A', color: '#F8F8F8'}} onClick={() => {
            loadMoreMovies();
          }}>Load More</Button>
        )}
      </Box>
    </>
  );
}
