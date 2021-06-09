const general = document.querySelectorAll('.anim');
const specials = document.querySelectorAll('.special-bits');
const appear_btns = document.querySelectorAll('.appears');
const hambuger = document.querySelector('.hambuger-main').addEventListener('click', activate);
const nav_list = document.querySelector('.nav_items');
const about_btn = document.getElementById('#about').addEventListener('click', showAbout);
const about_section = document.getElementById('#about-section');
const options = {
    root: null,
    threshold: 0.5,
    rootMargin: "0px"
}


// Navigation animation on clicking hambuger
function activate(e){
    e.preventDefault;
    nav_list.classList.toggle('active');
}

// Show in-page about section
function showAbout(e){
    // e.preventDefault();
    nav_list.classList.remove('active');

}

// activate();

const general_observer = new IntersectionObserver((entries, general_observer)=>{
    entries.forEach(entry =>{
        if (entry.isIntersecting){
            entry.target.style.animation = `gen_anim 1s ${entry.target.dataset.delay}  ease-in-out forwards`
        }
    })
}, options)

general.forEach(anim=>{
    general_observer.observe(anim)
})

const sp_options = {
    root: null,
    threshold: 0.6,
    rootMargin: "0px"
}

const bits_observer = new IntersectionObserver((entries, bits_observer)=>{
    entries.forEach(entry=>{
        if (entry.isIntersecting){
            entry.target.style.animation = `specials 500ms ${entry.target.dataset.delay} ease-in-out forwards`
        }
    })
}, sp_options)

specials.forEach(special=>{
    bits_observer.observe(special)
})

const appears_observer = new IntersectionObserver((entries, appears_observe)=>{
    entries.forEach(entry=>{
        if (entry.isIntersecting){
            entry.target.style.animation = `appears 1s ${entry.target.dataset.delay} ease-in-out forwards`
        }
    })
}, options)

appear_btns.forEach(appear=>{
    appears_observer.observe(appear)
})