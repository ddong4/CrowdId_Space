/* eslint-disable no-empty-pattern */
/* eslint-disable no-undef */
/* eslint-disable react/jsx-no-undef */
/* eslint-disable no-unused-vars */

function LandingPage(props) {
  // TODO:
  const {} = props;

  return (
    <div className="main-page">
      <a href="/video"> Video Test </a>
    </div>
  );
}

const landingPageData = {
  // TODO:
};

function App() {
  return <LandingPage {...landingPageData} />;
}

export default App;
