import {
    defineStore
} from "pinia";
import {
    ref,
    computed
} from 'vue'

export default defineStore('store', () => {
    const hello = ref(2)
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
    const doubleCount = computed(() => hello.value * 2)

    return {
        cardChecker
    }
})