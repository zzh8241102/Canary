import axios from "axios"

///// instance //////
const $http = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    timeout: 1000,
})

// before request
$http.interceptors.request.use(function (config) {
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

// 输出做了拦截的实例




export default $http
