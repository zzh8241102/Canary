import {
    defineStore
} from "pinia";
import {
    ref,
    computed,reactive
} from 'vue'

export default defineStore('store', () => {

    const loggedError = ref(false)
    const setLogged = ref(false)
    const smallCard = ref(350)
    // const isJumped = ref
    const smallWindowIndicator = ref(false)
    const cardChecker = () => {
        if (smallWindowIndicator.value) {
            smallCard.value = 350
        } else{
            smallCard.value = 250
        }
    }
    ////////////////////////////////////////////////////    
    ////////////////////////////////////////////////////
    
    const userInfo = reactive({
        username: '',
        email: '',
    })

    const setUserInfo = (username, email) => {
        userInfo.username = username
        userInfo.email = email
    }
    const getUserInfo = () => {
        return userInfo
    }

    
    return {
        setUserInfo,
        cardChecker,
        getUserInfo
    }
})