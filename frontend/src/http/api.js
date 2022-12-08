import $http from "./index.js";

// export const getFakeData = $http.get('https://jsonplaceholder.typicode.com/todos/1')

export const  helloWorld = $http.get('api/test')
// Apis for user Login and Register
export const login = (data) => $http.post('/api/signin', data)
export const register = (data) => $http.post('/api/register', data)
// Apis for articleslist
export const getArticlesList = (data) => $http.get('/api/articleslist', data)
// /api/articleslist?tag=tagname
export const getArticlesListByTag = (data) => $http.get('/api/articleslist', data)
// /api/articleslist?user=username
export const getArticlesListByUser = (data) => $http.get('/api/articleslist', data)
// /api/article?article_id=article_id
export const getArticle = (data) => $http.get('/api/article', data)
// api/tags
export const getTags = (data) => $http.get('/api/tags', data)

// /api/post
export const postArticle = (data) => $http.post('/api/post', data)
// /api/comment
export const postComment = (data) => $http.post('/api/comment', data)
