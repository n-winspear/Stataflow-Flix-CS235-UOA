import React from "react";
import { Route } from "react-router-dom";
import Home from "components/home/Home";
import MovieDetails from "components/movieDetails/MovieDetails";

export default function PageRouter({ apiURL }) {
  return (
    <>
      <Route
        exact
        path="/movie/:movieID"
        render={(props) => <MovieDetails {...props} apiURL={apiURL} />}
      />
      <Route
        exact
        path="/"
        render={(props) => <Home {...props} apiURL={apiURL} />}
      />
    </>
  );
}
