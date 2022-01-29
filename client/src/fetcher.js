import config from './config.json';

const getCloseObjects = async (loc) => {
  var res = await fetch(
    `http://${config.server_host}:${config.server_port}/results/loc?loc=${loc}`,
    {
      method: 'GET'
    }
  );
  return res.json();
};
