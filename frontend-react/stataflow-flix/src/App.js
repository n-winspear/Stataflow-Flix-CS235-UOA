import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import NavBar from "components/NavBar";
import PageRouter from "components/PageRouter";

const apiVersion = 1;
const apiURL = `http://127.0.0.1:5000/v${apiVersion}`;
const userID = "d4dff177-474e-4123-a3f9-8f0758114f25";

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
