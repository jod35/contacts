const modalOpenButton=document.querySelector('.open-btn');
const contactModal=document.querySelector('.add-modal');


modalOpenButton.addEventListener('click',()=>{
    contactModal.style.display="block";
})


const closeModal=(id)=>{
    let element=document.getElementById(id);

    element.style.display="none";
}