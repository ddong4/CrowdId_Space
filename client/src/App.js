import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import VideoPage from './pages/VideoPage';

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route path="/" exact component={LandingPage} />
          <Route path="/survey" exact component={VideoPage} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
