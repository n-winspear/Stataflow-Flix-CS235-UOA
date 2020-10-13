import React from "react";
import { Route } from "react-router-dom";
import Home from "components/home/Home";
import MovieDetails from "components/movieDetails/MovieDetails";

export default function PageRouter({ apiURL, userID }) {
  return (
    <>
      <Route
        exact
        path="/movies/:movieID"
        render={(props) => <MovieDetails {...props} apiURL={apiURL} userID={userID} />}
      />
      <Route
        exact
        path="/"
        render={(props) => <Home {...props} apiURL={apiURL} userID={userID} />}
      />
    </>
  );
}
