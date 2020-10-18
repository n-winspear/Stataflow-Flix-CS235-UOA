import React, {useEffect} from "react";
import { Route } from "react-router-dom";
import Home from "components/home/Home";
import NavBar from "components/NavBar";
import MovieDetails from "components/movieDetails/MovieDetails";
import Cookies from 'universal-cookie'

export default function PageRouter(props) {
  const { apiURL, userID, userAuthorised, setUserID, setUserAuthorised } = props;
  const cookies = new Cookies();

  useEffect(() => {
    if(!userAuthorised) {
      if (cookies.get('userID')) {
        setUserID(cookies.get('userID'))
        setUserAuthorised(true)
      } else {
        props.history.push('/login')
      }
    }
  })

  return (
    <>
      <NavBar setUserAuthorised={setUserAuthorised} setUserID={setUserID} />
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
