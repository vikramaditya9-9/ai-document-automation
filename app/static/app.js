/**
 * DocuFlow AI - Main Application
 */

class DocuFlowApp {
  constructor() {
    this.currentUser = null;
    this.currentPage = 'login';
    this.init();
  }

  async init() {
    // Check if user is logged in
    await this.checkAuth();
    this.renderNavbar();
    this.renderPage();
  }

  async checkAuth() {
    try {
      const response = await fetch('/api/auth/me');
      if (response.ok) {
        this.currentUser = await response.json();
      } else {
        this.currentUser = null;
      }
    } catch (error) {
      console.log('Not authenticated');
      this.currentUser = null;
    }
  }

  async renderNavbar() {
    const navRight = document.getElementById('navRight');
    navRight.innerHTML = '';

    if (!this.currentUser) {
      navRight.innerHTML = `
        <a href="#" class="nav-link" onclick="app.goToPage('login'); return false;">Login</a>
        <a href="#" class="nav-link" onclick="app.goToPage('register'); return false;">Register</a>
      `;
    } else {
      navRight.innerHTML = `
        <div class="nav-user">
          <span class="nav-link">${this.currentUser.full_name || this.currentUser.email}</span>
          <button class="logout-btn" onclick="app.logout()">Logout</button>
        </div>
      `;
    }
  }

  goToPage(page) {
    this.currentPage = page;
    this.renderPage();
  }

  renderPage() {
    const content = document.getElementById('content');

    if (!this.currentUser && this.currentPage !== 'login' && this.currentPage !== 'register') {
      this.currentPage = 'login';
    }

    if (this.currentUser && (this.currentPage === 'login' || this.currentPage === 'register')) {
      this.currentPage = 'dashboard';
    }

    switch (this.currentPage) {
      case 'login':
        content.innerHTML = this.renderLoginPage();
        break;
      case 'register':
        content.innerHTML = this.renderRegisterPage();
        break;
      case 'dashboard':
        content.innerHTML = this.renderDashboardPage();
        break;
      case 'upload':
        content.innerHTML = this.renderUploadPage();
        break;
      case 'documents':
        content.innerHTML = this.renderDocumentsPage();
        this.loadDocuments();
        break;
      default:
        this.currentPage = 'login';
        this.renderPage();
    }
  }

  renderLoginPage() {
    return `
      <div class="grid">
        <div></div>
        <div>
          <h1 class="text-center">Login</h1>
          <div class="card">
            <form onsubmit="app.handleLogin(event)">
              <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
              </div>
              <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
              </div>
              <button type="submit" class="btn btn-primary btn-block">Login</button>
            </form>
            <div class="text-center mt-3">
              <span>Don't have an account? <a href="#" onclick="app.goToPage('register'); return false;">Register</a></span>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    `;
  }

  renderRegisterPage() {
    return `
      <div class="grid">
        <div></div>
        <div>
          <h1 class="text-center">Create Account</h1>
          <div class="card">
            <form onsubmit="app.handleRegister(event)">
              <div class="form-group">
                <label for="full_name">Full Name</label>
                <input type="text" id="full_name" name="full_name" required>
              </div>
              <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
              </div>
              <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
              </div>
              <button type="submit" class="btn btn-primary btn-block">Register</button>
            </form>
            <div class="text-center mt-3">
              <span>Already have an account? <a href="#" onclick="app.goToPage('login'); return false;">Login</a></span>
            </div>
          </div>
        </div>
        <div></div>
      </div>
    `;
  }

  renderDashboardPage() {
    return `
      <div>
        <h1>Welcome, ${this.currentUser.full_name || this.currentUser.email}!</h1>
        <div class="grid grid-2 mt-3">
          <div class="card">
            <div class="card-title">Upload Document</div>
            <p class="mt-2">Upload a new document for processing</p>
            <button class="btn btn-primary" onclick="app.goToPage('upload')">Upload Now</button>
          </div>
          <div class="card">
            <div class="card-title">My Documents</div>
            <p class="mt-2">View all your uploaded documents</p>
            <button class="btn btn-secondary" onclick="app.goToPage('documents')">View Documents</button>
          </div>
        </div>
      </div>
    `;
  }

  renderUploadPage() {
    return `
      <div class="grid">
        <div></div>
        <div>
          <h1>Upload Document</h1>
          <div class="card">
            <form onsubmit="app.handleFileUpload(event)">
              <div class="form-group">
                <label>Select a file</label>
                <div class="file-input-wrapper">
                  <label class="file-input-label" id="fileDropZone">
                    <div class="file-input-text">
                      <div class="file-input-icon">📄</div>
                      <p>Drag and drop your file here or click to browse</p>
                      <small>Supported: PDF, PNG, JPG, JPEG</small>
                    </div>
                  </label>
                  <input type="file" id="fileInput" class="file-input" accept=".pdf,.png,.jpg,.jpeg">
                </div>
              </div>
              <div id="fileInfo" class="hidden mt-2">
                <p><strong>File:</strong> <span id="fileName"></span></p>
              </div>
              <div id="uploadMessage" class="hidden mt-2"></div>
              <button type="submit" class="btn btn-primary btn-block mt-3">Upload Document</button>
              <button type="button" class="btn btn-secondary btn-block mt-2" onclick="app.goToPage('dashboard')">Cancel</button>
            </form>
          </div>
        </div>
        <div></div>
      </div>
    `;
  }

  renderDocumentsPage() {
    return `
      <div>
        <h1>My Documents</h1>
        <button class="btn btn-primary mb-3" onclick="app.goToPage('upload')">Upload New Document</button>
        <div id="documentsList"></div>
      </div>
    `;
  }

  async handleLogin(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });

      if (response.ok) {
        await this.checkAuth();
        this.renderNavbar();
        this.goToPage('dashboard');
      } else {
        const error = await response.json();
        alert(error.detail || 'Login failed');
      }
    } catch (error) {
      alert('Error: ' + error.message);
    }
  }

  async handleRegister(event) {
    event.preventDefault();
    const full_name = document.getElementById('full_name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
      const response = await fetch('/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ full_name, email, password }),
      });

      if (response.ok) {
        alert('Registration successful! Please login.');
        this.goToPage('login');
      } else {
        const error = await response.json();
        alert(error.detail || 'Registration failed');
      }
    } catch (error) {
      alert('Error: ' + error.message);
    }
  }

  async handleFileUpload(event) {
    event.preventDefault();
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
      alert('Please select a file');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    const messageDiv = document.getElementById('uploadMessage');
    messageDiv.classList.remove('hidden');

    try {
      const response = await fetch('/api/documents/upload', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        messageDiv.innerHTML = '<div class="alert alert-success">Document uploaded successfully!</div>';
        setTimeout(() => {
          this.goToPage('documents');
        }, 2000);
      } else {
        const error = await response.json();
        messageDiv.innerHTML = `<div class="alert alert-error">${error.detail || 'Upload failed'}</div>`;
      }
    } catch (error) {
      messageDiv.innerHTML = `<div class="alert alert-error">Error: ${error.message}</div>`;
    }
  }

  async loadDocuments() {
    const documentsList = document.getElementById('documentsList');
    documentsList.innerHTML = '<div class="loading"></div>';

    try {
      const response = await fetch('/api/documents/');
      if (response.ok) {
        const documents = await response.json();
        this.renderDocumentsList(documents);
      } else {
        documentsList.innerHTML = '<div class="alert alert-error">Failed to load documents</div>';
      }
    } catch (error) {
      documentsList.innerHTML = `<div class="alert alert-error">Error: ${error.message}</div>`;
    }
  }

  renderDocumentsList(documents) {
    const documentsList = document.getElementById('documentsList');

    if (documents.length === 0) {
      documentsList.innerHTML = `
        <div class="card text-center">
          <p>No documents uploaded yet.</p>
          <button class="btn btn-primary" onclick="app.goToPage('upload')">Upload Your First Document</button>
        </div>
      `;
      return;
    }

    let html = '<div class="grid">';
    documents.forEach((doc) => {
      html += `
        <div class="card">
          <div class="card-header">
            <div>
              <h3 class="card-title">${doc.original_filename}</h3>
              <small>${new Date(doc.created_at).toLocaleDateString()}</small>
            </div>
            <span class="badge badge-${doc.status === 'APPROVED' ? 'success' : doc.status === 'REJECTED' ? 'error' : 'info'}">${doc.status}</span>
          </div>
          <div class="card-body">
            <p><strong>Type:</strong> ${doc.document_type || 'Not classified'}</p>
          </div>
          <div class="card-footer">
            <button class="btn btn-secondary" onclick="app.viewDocument(${doc.id})">View Details</button>
            <button class="btn btn-danger" onclick="app.deleteDocument(${doc.id})">Delete</button>
          </div>
        </div>
      `;
    });
    html += '</div>';
    documentsList.innerHTML = html;
  }

  viewDocument(documentId) {
    alert('Document details view coming soon! (ID: ' + documentId + ')');
  }

  async deleteDocument(documentId) {
    if (!confirm('Are you sure you want to delete this document?')) return;

    try {
      const response = await fetch(`/api/documents/${documentId}`, {
        method: 'DELETE',
      });

      if (response.ok) {
        alert('Document deleted successfully');
        this.loadDocuments();
      } else {
        alert('Failed to delete document');
      }
    } catch (error) {
      alert('Error: ' + error.message);
    }
  }

  async logout() {
    try {
      await fetch('/api/auth/logout', { method: 'POST' });
      this.currentUser = null;
      this.currentPage = 'login';
      this.renderNavbar();
      this.renderPage();
    } catch (error) {
      alert('Error logging out: ' + error.message);
    }
  }
}

// Initialize app when DOM is ready
let app;
document.addEventListener('DOMContentLoaded', () => {
  app = new DocuFlowApp();
});

// File drag and drop
document.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    const fileDropZone = document.getElementById('fileDropZone');
    const fileInput = document.getElementById('fileInput');

    if (fileDropZone) {
      fileDropZone.addEventListener('click', () => fileInput.click());

      fileDropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        fileDropZone.classList.add('drag-over');
      });

      fileDropZone.addEventListener('dragleave', () => {
        fileDropZone.classList.remove('drag-over');
      });

      fileDropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        fileDropZone.classList.remove('drag-over');
        fileInput.files = e.dataTransfer.files;
        const fileInfo = document.getElementById('fileInfo');
        document.getElementById('fileName').textContent = fileInput.files[0]?.name || '';
        fileInfo.classList.remove('hidden');
      });

      fileInput.addEventListener('change', () => {
        const fileInfo = document.getElementById('fileInfo');
        document.getElementById('fileName').textContent = fileInput.files[0]?.name || '';
        fileInfo.classList.remove('hidden');
      });
    }
  }, 100);
});
