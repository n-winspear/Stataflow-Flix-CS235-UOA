import React from "react";
import { Box, Grid } from "@material-ui/core";
import MovieCard from "components/home/MovieCard";
import { makeStyles, useTheme } from "@material-ui/core/styles";

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
  const theme = useTheme();

  return (
    <Box className={classes.root}>
      <Grid container justify={"center"} spacing={2}>
        <Grid item xs={12} sm={6} md={4} lg={3} xl={2}>
          <MovieCard />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3} xl={2}>
          <MovieCard />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3} xl={2}>
          <MovieCard />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3} xl={2}>
          <MovieCard />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3} xl={2}>
          <MovieCard />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3} xl={2}>
          <MovieCard />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3} xl={2}>
          <MovieCard />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3} xl={2}>
          <MovieCard />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3} xl={2}>
          <MovieCard />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3} xl={2}>
          <MovieCard />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3} xl={2}>
          <MovieCard />
        </Grid>
        <Grid item xs={12} sm={6} md={4} lg={3} xl={2}>
          <MovieCard />
        </Grid>
      </Grid>
    </Box>
  );
}
