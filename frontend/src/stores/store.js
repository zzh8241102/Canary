import { defineStore } from "pinia";
import {ref,computed} from 'vue'

export default defineStore('store', () => {
    const hello = ref(2)
    const loggedError = ref(false)
    const increment = () => {
        hello.value++
    }
    const doubleCount = computed(() => hello.value * 2)
    
    return {
        increment,
    }
})