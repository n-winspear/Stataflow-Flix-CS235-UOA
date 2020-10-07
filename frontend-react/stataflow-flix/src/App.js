import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import NavBar from "components/NavBar";
import PageRouter from "components/PageRouter";

const apiVersion = 1;
const apiURL = `api.stataflow.com/v${apiVersion}`;
const userID = "1";

function App() {
  return (
    <Router>
      <NavBar />
      <Switch>
        <Route
          path="/"
          render={(props) => (
            <PageRouter {...props} apiURL={apiURL} userID={userID} />
          )}
        />
      </Switch>
    </Router>
  );
}

export default App;
