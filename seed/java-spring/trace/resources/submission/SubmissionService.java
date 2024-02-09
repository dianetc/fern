/**
 * This file was auto-generated by Fern from our API Definition.
 */

package resources.submission;

import java.lang.String;
import java.util.Optional;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import resources.commons.types.Language;
import resources.submission.types.ExecutionSessionResponse;
import resources.submission.types.GetExecutionSessionStateResponse;

@RequestMapping(
    path = "/sessions"
)
public interface SubmissionService {
  @PostMapping(
      value = "/create-session/{language}",
      produces = "application/json"
  )
  ExecutionSessionResponse createExecutionSession(
      @RequestHeader("X-Random-Header") Optional<String> xRandomHeader,
      @PathVariable("language") Language language);

  @GetMapping(
      value = "/{sessionId}",
      produces = "application/json"
  )
  Optional<ExecutionSessionResponse> getExecutionSession(
      @RequestHeader("X-Random-Header") Optional<String> xRandomHeader,
      @PathVariable("sessionId") String sessionId);

  @DeleteMapping("/stop/{sessionId}")
  void stopExecutionSession(@RequestHeader("X-Random-Header") Optional<String> xRandomHeader,
      @PathVariable("sessionId") String sessionId);

  @GetMapping(
      value = "/execution-sessions-state",
      produces = "application/json"
  )
  GetExecutionSessionStateResponse getExecutionSessionsState(
      @RequestHeader("X-Random-Header") Optional<String> xRandomHeader);
}