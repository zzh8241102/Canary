import axios from "axios"

///// instance //////
const $http = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    timeout: 1000,
})

// before request
$http.interceptors.request.use(function (config) {
    config.headers.Authorization = localStorage.getItem('access_token')
    console.log(localStorage.getItem('access_token'))
    return config;
  }, function (error) {
    // error handling
    return Promise.reject(error);
});

// after response
axios.interceptors.response.use(function (response) {
    // handle the response data
    return response;
  }, function (error) {
    // handle the response error
    return Promise.reject(error);
  });






export default $http
