import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "components/home/Home";
import NavBar from "components/NavBar";

const apiVersion = 1;
const apiURL = `http://127.0.0.1:5000/api/v${apiVersion}`;

function App() {
  return (
    <Router>
      <NavBar />
      <Switch>
        <Route
          exact
          path="/movies/:movieID"
          render={(props) => <MovieDetails {...props} apiURL={apiURL} />}
        />
        <Route
          exact
          path="/"
          render={(props) => <Home {...props} apiURL={apiURL} />}
        />
      </Switch>
    </Router>
  );
}

export default App;
