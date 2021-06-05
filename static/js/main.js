const general = document.querySelectorAll('.anim');
const specials = document.querySelectorAll('.special-bits');
const options = {
    root: null,
    threshold: .5,
    rootMargin: "0px"
}

const general_observer = new IntersectionObserver((entries, general_observer)=>{
    entries.forEach(entry =>{
        if (entry.isIntersecting){
            entry.target.style.animation = `gen_anim 1s ease-in-out forwards`
        }
    })
}, options)

general.forEach(anim=>{
    general_observer.observe(anim)
})

const sp_options = {
    root: null,
    threshold: 1,
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