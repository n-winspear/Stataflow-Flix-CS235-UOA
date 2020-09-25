import React, { useState, useEffect } from "react";
import { Box } from '@material-ui/core';
import { makeStyles } from "@material-ui/core/styles";
import CircularProgress from "@material-ui/core/CircularProgress";

const useStyles = makeStyles(() => ({
  loading: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    flexGrow: 1,
    height: "calc(100vh - 64px)",
  },
  circularProgress: {
    color: "#FDA74A",
  },
}));

export default function MovieDetails(props) {
  const { match } = props;
  const classes = useStyles();
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    function loadData() {
      setTimeout(() => {
        setLoading(false)
      },1000);
    }
    loadData();
  });

  return isLoading ? (
    <Box className={classes.loading}>
      <CircularProgress className={classes.circularProgress} />
    </Box>
  ) : (
    <div>
      <h1>{match.params.movieID}</h1>
    </div>
    
  );

}
