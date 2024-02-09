/**
 * This file was auto-generated by Fern from our API Definition.
 */

package resources.commons.types;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import core.ObjectMappers;
import java.lang.Object;
import java.lang.String;
import java.util.Objects;

@JsonInclude(JsonInclude.Include.NON_EMPTY)
@JsonDeserialize(
    builder = SinglyLinkedListNodeAndListValue.Builder.class
)
public final class SinglyLinkedListNodeAndListValue {
  private final NodeId nodeId;

  private final SinglyLinkedListValue fullList;

  private SinglyLinkedListNodeAndListValue(NodeId nodeId, SinglyLinkedListValue fullList) {
    this.nodeId = nodeId;
    this.fullList = fullList;
  }

  @JsonProperty("nodeId")
  public NodeId getNodeId() {
    return nodeId;
  }

  @JsonProperty("fullList")
  public SinglyLinkedListValue getFullList() {
    return fullList;
  }

  @java.lang.Override
  public boolean equals(Object other) {
    if (this == other) return true;
    return other instanceof SinglyLinkedListNodeAndListValue && equalTo((SinglyLinkedListNodeAndListValue) other);
  }

  private boolean equalTo(SinglyLinkedListNodeAndListValue other) {
    return nodeId.equals(other.nodeId) && fullList.equals(other.fullList);
  }

  @java.lang.Override
  public int hashCode() {
    return Objects.hash(this.nodeId, this.fullList);
  }

  @java.lang.Override
  public String toString() {
    return ObjectMappers.stringify(this);
  }

  public static NodeIdStage builder() {
    return new Builder();
  }

  public interface NodeIdStage {
    FullListStage nodeId(NodeId nodeId);

    Builder from(SinglyLinkedListNodeAndListValue other);
  }

  public interface FullListStage {
    _FinalStage fullList(SinglyLinkedListValue fullList);
  }

  public interface _FinalStage {
    SinglyLinkedListNodeAndListValue build();
  }

  @JsonIgnoreProperties(
      ignoreUnknown = true
  )
  public static final class Builder implements NodeIdStage, FullListStage, _FinalStage {
    private NodeId nodeId;

    private SinglyLinkedListValue fullList;

    private Builder() {
    }

    @java.lang.Override
    public Builder from(SinglyLinkedListNodeAndListValue other) {
      nodeId(other.getNodeId());
      fullList(other.getFullList());
      return this;
    }

    @java.lang.Override
    @JsonSetter("nodeId")
    public FullListStage nodeId(NodeId nodeId) {
      this.nodeId = nodeId;
      return this;
    }

    @java.lang.Override
    @JsonSetter("fullList")
    public _FinalStage fullList(SinglyLinkedListValue fullList) {
      this.fullList = fullList;
      return this;
    }

    @java.lang.Override
    public SinglyLinkedListNodeAndListValue build() {
      return new SinglyLinkedListNodeAndListValue(nodeId, fullList);
    }
  }
}