const general = document.querySelectorAll('.anim');

const options = {
    root: null,
    threshold: .5,
    rootMargin: "0px"
}

const general_observer = new IntersectionObserver((entries, general_observer)=>{
    entries.forEach(entry =>{
        if (entry.isIntersecting){
            entry.target.style.animation = 'gen_anim 2s ease-in-out forwards'
        }
    })
}, options)

general.forEach(anim=>{
    general_observer.observe(anim)
})