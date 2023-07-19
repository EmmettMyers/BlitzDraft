import { getAuth, signInWithPopup, GoogleAuthProvider, signInWithRedirect } from "firebase/auth";
import { initializeApp } from 'firebase/app';
import { ref } from "vue";

const firebaseConfig = {
    apiKey: { HIDDEN },
    authDomain: { HIDDEN },
    projectId: { HIDDEN },
    storageBucket: { HIDDEN },
    messagingSenderId: { HIDDEN },
    appId: { HIDDEN },
    measurementId: { HIDDEN }
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
