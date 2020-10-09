import React from "react";
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Welcome from "./welcome";
import Dashboard from "./dashboard";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="App">
        <Route exact path="/" component={Welcome} /> 
        <Route path="/dashboard" component={Dashboard} />
      </div>
    </Router>
  );
}

export default App;
