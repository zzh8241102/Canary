import $http from "./index.js";
import $img from "./index.js";

// export const getFakeData = $http.get('https://jsonplaceholder.typicode.com/todos/1')

export const  helloWorld = $http.get('api/test')
// Apis for user Login and Register
export const login = (data) => $http.post('/api/signin', data)
export const register = (data) => $http.post('/api/register', data)
// Apis for articleslist
// here the data should contain the limit, which is initally hardcoded to 15
export const getArticlesList = (data) => $http.get('/api/articleslist', data)

// /api/user?user=username 
export const getUserInfo = (data) => $http.get('/api/user', data)

// 
export const addNewTag = (data) => $http.post('/api/addtag', data)

export const deleteAccount = (data) => $http.post('/api/user/delete', data)

export const changeUserInfo = (data) => $http.post('/api/user/change', data)

// /api/tags?user=username
export const getUserTags = (data) => $http.get('/api/tags', data)

// /api/user/change/password
export const changePassword = (data) => $http.post('/api/user/change/password', data)
// /api/articleslist?tag=tagname
export const getArticlesListByTag = (data) => $http.get('/api/articleslist/tag', data)
// /api/article?article_id=article_id
export const getArticle = (data) => $http.get('/api/article', data)
// api/tags
export const getTags = (data) => $http.get('/api/alltags', data)

// /api/post
export const postArticle = (data) => $http.post('/api/post', data)

// submit like by article
export const submitLike = (data) => $http.post('/api/like', data)

// /api/comment?article_id=article_id
export const getComments = (data) => $http.get('/api/comment', data)
// /api/postcomment
export const postComment = (data) => $http.post('/api/postcomment', data)
// /api/search?search=keyword
export const searchCon = (data) => $http.get('/api/search', data)

// /api/findtag
export const findArticleTag = (data) => $http.get('/api/findtag', data)


// /api/user/activity
export const getUserActivity = (data) => $http.get('/api/user/activity', data)

// /api/findtaginfo
export const getTagInfo = (data) => $http.get('/api/findtaginfo', data)

// UserInfoStatsApi UserInfoStatsApi
export const getUserInfoStats = (data) => $http.get('/api/user/stats', data)

// /api/user/followtag
export const followTag = (data) => $http.post('/api/user/followtag', data)

// /api/tag/follower'
export const getTagFollower = (data) => $http.get('/api/tag/follower', data)

// /api/user/unfollowtag
export const unFollowTag = (data) => $http.post('/api/user/unfollowtag', data)

// /api/find/avatar
export const getAvatar = (data) => $http.get('/api/find/avatar', data) 


