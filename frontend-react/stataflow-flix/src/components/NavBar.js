import React from "react";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import { useHistory } from "react-router-dom";
import Cookies from 'universal-cookie'
import { Button } from '@material-ui/core'

const useStyles = makeStyles((theme) => ({
  head: {
    flexGrow: 1,
  },
  appBar: {
    background: "linear-gradient(90deg, #FDA74A, #FF6372)",
  },
  menuButton: {
    marginRight: theme.spacing(2),
    marginLeft: "auto"
  },
  title: {
    display: "none",
    [theme.breakpoints.up("sm")]: {
      display: "block",
    },
    "&:hover": {
      cursor: "pointer",
    },
  },
}));

export default function SearchAppBar(props) {
  const classes = useStyles();
  const history = useHistory();
  const cookies = new Cookies()
  const { setUserAuthorised, setUserID } = props;

  return (
    <div className={classes.head}>
      <AppBar position="static" className={classes.appBar}>
        <Toolbar>
          <Typography
            className={classes.title}
            variant="h5"
            noWrap
            onClick={() => history.push("/")}
          >
            Stataflow Flix
          </Typography>
          <Button
            edge="start"
            className={classes.menuButton}
            color="inherit"
            aria-label="open drawer"
            onClick={() => {
              cookies.remove('userID')
              setUserID('')
              setUserAuthorised(false)
            }}
          >
            Logout
          </Button>
        </Toolbar>
      </AppBar>
    </div>
  );
}
