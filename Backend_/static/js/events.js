function initializeMenuFunctionality() {
    const toggleMenu = document.querySelector('.toggle-menu');
    const menuList = document.querySelector('.menu ul');
    const toggleCloseMenu = document.querySelector('.close-menu');
  
    toggleMenu.addEventListener('click', () => {
      menuList.classList.toggle('show');
      toggleCloseMenu.classList.toggle('show');
      toggleMenu.classList.add('hidden');
    });
  
    toggleCloseMenu.addEventListener('click', () => {
      menuList.classList.remove('show');
      toggleCloseMenu.classList.remove('show');
      toggleMenu.classList.remove('hidden');
    });
  }
  