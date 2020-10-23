import React, {useState, useEffect} from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import PageRouter from "components/PageRouter";
import LoginPage from 'components/userAuth/LoginPage'
import RegisterPage from 'components/userAuth/RegisterPage'
import Cookies from 'universal-cookie';

const apiVersion = 1;
//const apiURL = `http://127.0.0.1:5000/v${apiVersion}`;
const apiURL = `http://ifce.stataflow.com/v${apiVersion}`;


function App() {
  const [userAuthorised, setUserAuthorised] = useState(false)
  const [userID, setUserID] = useState(null)
  const cookies = new Cookies();
  
  
  useEffect(() => {
    if (cookies.get('userID')) {
      setUserID(cookies.get('userID'))
      setUserAuthorised(true)
    } else if (userID) {
      cookies.set('userID', userID, {path: '/'})
    }
  }, [cookies, userID, userAuthorised])

  console.log(apiURL)
  
  return (
    <Router>
      <Switch>
        <Route
          path="/register"
          exact
          render={(props) => (
            <RegisterPage {...props} apiURL={apiURL} setUserAuthorised={setUserAuthorised} setUserID={setUserID} />
          )}
        />
        <Route
          path="/login"
          exact
          render={(props) => (
            <LoginPage {...props} apiURL={apiURL} setUserAuthorised={setUserAuthorised} setUserID={setUserID} />
          )}
        />
        <Route
          path="/"
          render={(props) => (
            <PageRouter {...props} apiURL={apiURL} userID={userID} userAuthorised={userAuthorised} setUserAuthorised={setUserAuthorised} setUserID={setUserID} />
          )}
        />
      </Switch>
    </Router>
  );
}

export default App;
