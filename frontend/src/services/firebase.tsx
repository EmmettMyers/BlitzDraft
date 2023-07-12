import { getAuth, signInWithPopup, GoogleAuthProvider, signInWithRedirect } from "firebase/auth";
import { initializeApp } from 'firebase/app';
import { ref } from "vue";

const firebaseConfig = {
    apiKey: "AIzaSyDOiajHNEs808LK2IzDi5pUu1z5m8nTUXE",
    authDomain: "blitzdraft-10230.firebaseapp.com",
    projectId: "blitzdraft-10230",
    storageBucket: "blitzdraft-10230.appspot.com",
    messagingSenderId: "237050519023",
    appId: "1:237050519023:web:35ed944f39e31f39baaa1a",
    measurementId: "G-D0V6W3FNGL"
};

export const loggedIn = ref(false);

const app = initializeApp(firebaseConfig);
const provider = new GoogleAuthProvider();
const auth = getAuth();

export const googleSignIn = (): void => {
    signInWithPopup(auth, provider)
    .then((result) => {
        if (result.user.displayName && result.user.email){
            localStorage.setItem("username", result.user.displayName);
            localStorage.setItem("email", result.user.email);
            loggedIn.value = true;
        }
    }).catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        const email = error.customData.email;
        const credential = GoogleAuthProvider.credentialFromError(error);
    });
}

export const logOut = (): void => {
    localStorage.setItem("username", "");
    localStorage.setItem("email", "");
    loggedIn.value = false;
}