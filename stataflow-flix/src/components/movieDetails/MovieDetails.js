import React, { useState, useEffect } from "react";
import { Grid, Box, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import CircularProgress from "@material-ui/core/CircularProgress";
import MovieCoverPoster from "components/movieDetails/images/MovieCoverPoster.jpg";

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
}));

export default function MovieDetails(props) {
  const { match, location } = props;
  const movieData = location.state.movieData;
  const classes = useStyles();
  const [isLoading, setLoading] = useState(true);

  console.log(match);
  console.log(movieData);

  useEffect(() => {
    function loadData() {
      setTimeout(() => {
        setLoading(false);
      }, 1000);
    }
    loadData();
  });

  return isLoading ? (
    <Box className={classes.pageContent}>
      <CircularProgress className={classes.circularProgress} />
    </Box>
  ) : (
      <Box className={classes.pageContent}>
        <Grid container justify="center" alignItems="center">
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
            xl={3}
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
            </Grid>
            <Grid item xs={12}>
              <Box mt={2} ml={-20}>
                <Typography>Genres:</Typography>
                <Typography gutterBottom variant="h5">
                  {movieData.genres.map((genre, index) => {
                    let genreText =
                      index === movieData.genres.length - 1
                        ? genre
                        : `${genre}, `;
                    return genreText;
                  })}
                </Typography>
              </Box>
            </Grid>
          </Grid>
          <Grid
            container
            direction="column"
            justify="center"
            alignItems="flex-start"
            item
            xs={12}
            sm={6}
            md={8}
            lg={9}
            xl={9}
          >
            <Grid item xs={12}>
              <Typography>{movieData.title}</Typography>
            </Grid>
            <Grid container direction="row" item xs={12}>
              <Grid item xs={1}>
                <Typography>{movieData.releaseYear}</Typography>
              </Grid>
              <Grid item xs={1}>
                <Typography>{movieData.runtime}</Typography>
              </Grid>
              <Grid item xs={1}>
                <Typography>{movieData.rating}</Typography>
              </Grid>
            </Grid>
            <Grid item xs={12}>
              <Typography>{movieData.description}</Typography>
            </Grid>
            <Grid
              container
              direction="row"
              justify="flex-start"
              alignItems="center"
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
                {
                  movieData.actors.map((actor, index) => {
                    <Grid item xs={12}>
                      <Typography key={index}>{actor.fullName}</Typography>
                    </Grid>

                  })
                }
              </Grid>
              <Grid
                container
                direction="column"
                item
                xs={12}
                sm={6}
                md={8}
                lg={9}
                xl={9}
              >
                <Grid item xs={12}>
                  <Typography>Review</Typography>
                </Grid>
                <Grid item xs={12}>
                  <Typography>Review</Typography>
                </Grid>
                <Grid item xs={12}>
                  <Typography>Review</Typography>
                </Grid>
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </Box>
    );
}
