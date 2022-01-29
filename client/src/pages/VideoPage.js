/* eslint-disable no-unused-vars */
/* eslint-disable no-empty-pattern */
import VideoCapture from '../components/VideoCapture';

function VideoPage(props) {
  // TODO:
  const {} = props;

  return (
    <div className="main-page">
      <a href="/video"> Video Test </a>
    </div>
  );
}

const videoPageData = {
  // TODO:
};

function App() {
  return <VideoPage {...videoPageData} />;
}

export default App;
