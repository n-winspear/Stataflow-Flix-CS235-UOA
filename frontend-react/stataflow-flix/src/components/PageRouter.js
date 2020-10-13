import React, {useEffect} from "react";
import { Route } from "react-router-dom";
import Home from "components/home/Home";
import NavBar from "components/NavBar";
import MovieDetails from "components/movieDetails/MovieDetails";

export default function PageRouter(props) {

  const { apiURL, userID, userAuthorised } = props;

  useEffect(() => {
    if(!userAuthorised) {
      props.history.push('/login')
    }
  })

  return (
    <>
      <NavBar />
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
