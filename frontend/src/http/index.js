import axios from "axios"

// 一个实例 后续所有的请求都会使用这个实例 受配置的约束
const $http = axios.create({
    baseURL: 'http://127.0.0.1:5000/',
    timeout: 1000,
    // headers: {
    //     "Content-Type": "application/json",
    //     "Accept": "application/json"
    // }   
})
//  请求拦截器
$http.interceptors.request.use(function (config) {
    // 在发送请求之前做些什么
    return config;
  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
});

// // 响应拦截器
axios.interceptors.response.use(function (response) {
    // 对响应数据做点什么
    return response;
  }, function (error) {
    // 对响应错误做点什么
    return Promise.reject(error);
  });

// 输出做了拦截的实例
export default $http