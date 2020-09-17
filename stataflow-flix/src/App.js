import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from "components/home/Home";
import NavBar from "components/NavBar";

function App() {
  return (
    <Router>
      <NavBar />
      <Switch>
        <Route exact path="/" component={Home} />
      </Switch>
    </Router>
  );
}

export default App;
