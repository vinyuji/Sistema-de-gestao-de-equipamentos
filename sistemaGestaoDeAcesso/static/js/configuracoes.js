// static/js/configuracoes.js

// Função para aplicar as configurações salvas no localStorage
function applyStoredSettings() {
    const storedFontSize = localStorage.getItem('fontSize') || 'font-medium';
    const storedTheme = localStorage.getItem('theme') || 'theme-default';

    // Remove classes antigas antes de adicionar as novas
    document.body.classList.remove('font-small', 'font-medium', 'font-large');
    document.body.classList.remove('theme-default', 'theme-high-contrast');

    // Aplica as classes salvas ao body
    document.body.classList.add(storedFontSize);
    document.body.classList.add(storedTheme);
    
    // Atualiza os botões na página de configurações para refletir o estado atual
    updateActiveButtons(storedFontSize, storedTheme);
}

// Função para destacar os botões ativos na página de configurações
function updateActiveButtons(fontSize, theme) {
    // Remove a classe 'active' de todos os botões de configuração
    document.querySelectorAll('.btn-setting').forEach(btn => btn.classList.remove('active'));

    // Adiciona a classe 'active' aos botões correspondentes às configurações atuais
    const fontButton = document.getElementById(fontSize.replace('-', ''));
    if (fontButton) fontButton.classList.add('active');

    const themeButton = document.getElementById(theme.replace('-', ''));
    if (themeButton) themeButton.classList.add('active');
}

// Adiciona os listeners de evento quando o DOM estiver pronto
document.addEventListener('DOMContentLoaded', () => {
    // Aplica as configurações salvas assim que a página carrega
    applyStoredSettings();

    // Listeners para os botões de tamanho de fonte
    document.getElementById('font-small')?.addEventListener('click', () => {
        localStorage.setItem('fontSize', 'font-small');
        applyStoredSettings();
    });
    document.getElementById('font-medium')?.addEventListener('click', () => {
        localStorage.setItem('fontSize', 'font-medium');
        applyStoredSettings();
    });
    document.getElementById('font-large')?.addEventListener('click', () => {
        localStorage.setItem('fontSize', 'font-large');
        applyStoredSettings();
    });

    // Listeners para os botões de tema
    document.getElementById('theme-default')?.addEventListener('click', () => {
        localStorage.setItem('theme', 'theme-default');
        applyStoredSettings();
    });
    document.getElementById('theme-high-contrast')?.addEventListener('click', () => {
        localStorage.setItem('theme', 'theme-high-contrast');
        applyStoredSettings();
    });
    
    // Listener para o botão de resetar
    document.getElementById('reset-settings')?.addEventListener('click', () => {
        // Remove os itens do localStorage
        localStorage.removeItem('fontSize');
        localStorage.removeItem('theme');
        // Reaplica as configurações (que agora serão as padrões)
        applyStoredSettings();
    });
});