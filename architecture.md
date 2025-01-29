# OpenRouter Dashboard Architecture

## Current System
The dashboard currently provides model statistics visualization with these key components:
- Model search and selection system
- Provider statistics fetching
- Data visualization in tabular format

## Proposed Architecture Changes

### 1. Authentication Layer
```
┌─────────────────┐
│  Auth Manager   │
├─────────────────┤
│ - Store API Key │
│ - Validate Key  │
│ - Secure Access │
└─────────────────┘
```

#### Implementation Details:
- Add secure localStorage for API key
- Implement key validation on startup
- Add authentication state management

### 2. Model Inference System
```
┌───────────────────┐      ┌──────────────────┐      ┌────────────────┐
│   Input Handler   │──────▶   API Gateway    │──────▶  Response UI   │
├───────────────────┤      ├──────────────────┤      ├────────────────┤
│ - Prompt Input    │      │ - Request Router │      │ - Display Area │
│ - Model Selection │      │ - Error Handler  │      │ - Token Stats  │
└───────────────────┘      └──────────────────┘      └────────────────┘
```

#### Implementation Details:
- Add prompt input interface
- Implement streaming response handling
- Add token usage tracking
- Implement error boundary system

### 3. Provider Selection System
```
┌────────────────────┐      ┌─────────────────┐      ┌────────────────┐
│  Selection Logic   │──────▶  Cost Manager   │──────▶   Optimizer    │
├────────────────────┤      ├─────────────────┤      ├────────────────┤
│ - Provider Ranking │      │ - Price Limits  │      │ - Best Match   │
│ - Filter Options   │      │ - Usage Tracker │      │ - Fallbacks    │
└────────────────────┘      └─────────────────┘      └────────────────┘
```

#### Implementation Details:
- Implement provider ranking algorithms
- Add cost optimization logic
- Create fallback selection system

### 4. UI Components
```
┌─────────────────┐
│   Dashboard     │
├─────────────────┤
│ ┌─────────────┐ │
│ │ Stats View  │ │
│ └─────────────┘ │
│ ┌─────────────┐ │
│ │ Chat View   │ │
│ └─────────────┘ │
└─────────────────┘
```

#### Implementation Details:
- Add tabbed interface for stats/chat
- Implement responsive design
- Add loading states and animations

## Technical Implementation Plan

### Phase 1: Core Infrastructure

#### HTML Changes
```html
<!-- Add to OpenRouterApi.html -->
<div id="auth-section">
  <input type="password" id="api-key" placeholder="Enter OpenRouter API Key" />
  <button id="save-key">Save Key</button>
</div>

<div id="chat-interface" class="hidden">
  <div id="model-selector">
    <select id="model-dropdown"></select>
    <div id="provider-filters">
      <button data-sort="price">Sort by Price</button>
      <button data-sort="latency">Sort by Latency</button>
      <button data-sort="throughput">Sort by Throughput</button>
    </div>
  </div>
  
  <div id="chat-container">
    <div id="messages"></div>
    <div id="input-area">
      <textarea id="prompt-input" placeholder="Enter your prompt..."></textarea>
      <button id="send-prompt">Send</button>
    </div>
  </div>
  
  <div id="usage-stats">
    <span id="token-count">Tokens: 0</span>
    <span id="cost-estimate">Est. Cost: $0.00</span>
  </div>
</div>
```

#### CSS Enhancements
```css
/* Add to styles.min.css */
.hidden {
  display: none;
}

#chat-interface {
  margin-top: 20px;
  display: grid;
  grid-template-rows: auto 1fr auto;
  gap: 20px;
}

#model-selector {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

#chat-container {
  height: 400px;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  background: white;
}

#messages {
  height: 320px;
  overflow-y: auto;
  padding: 20px;
}

#input-area {
  display: flex;
  gap: 10px;
  padding: 10px;
  border-top: 1px solid #dee2e6;
}

#prompt-input {
  flex: 1;
  min-height: 40px;
  padding: 10px;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  resize: none;
}

#usage-stats {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  background: #f8f9fa;
  border-radius: 4px;
}
```

#### JavaScript Architecture
```javascript
// Core modules to add to app.min.js

class AuthManager {
  constructor() {
    this.keyStorageKey = 'openrouter_api_key';
  }
  
  async validateAndStoreKey(apiKey) {
    // Validate key with OpenRouter API
    // Store if valid
  }
  
  getStoredKey() {
    return localStorage.getItem(this.keyStorageKey);
  }
}

class ProviderSelector {
  constructor(providers) {
    this.providers = providers;
    this.sortCriteria = 'price';
  }
  
  rankProviders(criteria) {
    // Sort providers based on criteria
    return [...this.providers].sort((a, b) => {
      switch(criteria) {
        case 'price': return a.pricing.prompt - b.pricing.prompt;
        case 'latency': return a.stats.avg_latency - b.stats.avg_latency;
        case 'throughput': return b.stats.throughput - a.stats.throughput;
      }
    });
  }
  
  selectBestProvider(constraints) {
    // Apply constraints and return best match
  }
}

class InferenceManager {
  constructor(authManager) {
    this.authManager = authManager;
    this.endpoint = 'https://openrouter.ai/api/v1/chat/completions';
  }
  
  async generateCompletion(prompt, model, provider) {
    // Handle API request and streaming response
  }
  
  calculateTokenUsage(prompt, response) {
    // Estimate token usage and costs
  }
}

class UIManager {
  constructor() {
    // Initialize UI components
    // Set up event listeners
  }
  
  updateInterface(state) {
    // Update UI based on state changes
  }
  
  displayMessage(message, type) {
    // Add message to chat interface
  }
}
```

### Phase 2: Enhanced Features
1. Implement streaming responses with Server-Sent Events
2. Add provider fallback mechanisms
3. Implement usage tracking and cost optimization

### Phase 3: UI/UX Improvements
1. Add responsive design for mobile devices
2. Implement comprehensive error handling
3. Add loading states and animations

## API Integration

### OpenRouter API Endpoints
```
POST /api/v1/chat/completions
Headers:
  - Authorization: Bearer {api_key}
  - HTTP-Referer: {origin}
Body:
  {
    "model": "anthropic/claude-2",
    "messages": [{"role": "user", "content": "Hello"}]
  }
```

```
GET /api/frontend/models
Response:
  {
    "data": [
      {
        "id": "...",
        "name": "...",
        "pricing": {...},
        "context_length": 100000,
        "providers": [...]
      }
    ]
  }
```

```
GET /api/frontend/stats/endpoint
Query: ?permaslug={model_slug}
Response:
  {
    "data": [
      {
        "provider_name": "...",
        "stats": [...],
        "pricing": {...}
      }
    ]
  }
```

## Security Considerations

### API Key Management
1. Store API key in localStorage with encryption
2. Clear key on logout/session end
3. Validate key before operations
4. Never expose key in URLs or logs

### Rate Limiting
1. Implement client-side request throttling
2. Track usage against OpenRouter limits
3. Show warning when approaching limits
4. Queue requests if needed

### Error Handling
1. Validate all user inputs
2. Sanitize displayed responses
3. Implement retry logic with backoff
4. Show user-friendly error messages

## Performance Optimizations

### Response Streaming
1. Use Server-Sent Events for streaming
2. Implement chunked response handling
3. Show incremental updates in UI
4. Handle connection drops gracefully

### Provider Caching
1. Cache provider statistics
2. Implement LRU cache for responses
3. Cache model configurations
4. Regular cache invalidation

### State Management
1. Implement optimistic updates
2. Batch UI updates
3. Use virtual scrolling for long chats
4. Debounce frequent operations

## Testing Strategy

### Unit Tests
```javascript
// Provider Selection Tests
describe('ProviderSelector', () => {
  test('ranks providers by price correctly', () => {
    const selector = new ProviderSelector(mockProviders);
    const ranked = selector.rankProviders('price');
    expect(ranked[0].pricing.prompt).toBeLessThan(ranked[1].pricing.prompt);
  });
});

// Auth Manager Tests
describe('AuthManager', () => {
  test('validates API key format', () => {
    const auth = new AuthManager();
    expect(auth.isValidKeyFormat('sk-123')).toBe(true);
  });
});
```

### Integration Tests
1. Test complete chat flow
2. Verify provider selection logic
3. Test error handling scenarios
4. Validate streaming responses

### E2E Tests
1. Test UI interactions
2. Verify real API responses
3. Test rate limiting behavior
4. Validate error displays

## Implementation Guidelines

### Code Organization
```
src/
  ├── components/
  │   ├── Chat/
  │   ├── ModelSelector/
  │   └── Stats/
  ├── services/
  │   ├── auth.js
  │   ├── inference.js
  │   └── providers.js
  └── utils/
      ├── cache.js
      └── validation.js
```

### Development Process
1. Start with auth implementation
2. Add basic chat interface
3. Implement provider selection
4. Add advanced features
5. Polish UI/UX
6. Comprehensive testing

### Best Practices
1. Use TypeScript for type safety
2. Follow SOLID principles
3. Document all components
4. Write unit tests first
5. Regular security audits