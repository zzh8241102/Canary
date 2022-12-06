import $http from "./index.js";

// export const getFakeData = $http.get('https://jsonplaceholder.typicode.com/todos/1')

export const  helloWorld = $http.get('api/test')
export const login = (data) => $http.post('/api/signin', data)
export const register = (data) => $http.post('/api/register', data)