@RestController
public class ChatController {

    @PostMapping("/chat")
    public ResponseEntity<Map<String, Object>> chat(@RequestBody Map<String, String> payload) {
        String query = payload.get("query");
        
        // Use Gemini API here (or call your chatbot engine)
        String response = GeminiService.getResponse(query);
        
        Map<String, Object> result = new HashMap<>();
        result.put("message", response);
        result.put("escalate", false); // or true based on intent

        return ResponseEntity.ok(result);
    }
}
